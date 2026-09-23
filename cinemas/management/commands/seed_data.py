import random
from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from faker import Faker

from cinemas.models import Cinema, Hall, Seat
from movies.models import Movie
from showtimes.models import Showtime
from reservations.models import Reservation

User = get_user_model()


class Command(BaseCommand):
    help = "Create fake cinema reservation data"

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=100)
        parser.add_argument("--cinemas", type=int, default=5)
        parser.add_argument("--halls", type=int, default=3)
        parser.add_argument("--movies", type=int, default=20)
        parser.add_argument("--reservations", type=int, default=200)

    @transaction.atomic
    def handle(self, *args, **options):
        fake = Faker()

        users_count = options["users"]
        cinemas_count = options["cinemas"]
        halls_count = options["halls"]
        movies_count = options["movies"]
        reservations_count = options["reservations"]

        # =========================
        # Users
        # =========================

        users = []

        for i in range(users_count):
            username = f"user_{i + 1}"

            user, created = User.objects.get_or_create(
                username=username,
                defaults={
                    "email": fake.email(),
                    "first_name": fake.first_name(),
                    "last_name": fake.last_name(),
                },
            )

            if created:
                user.set_password("12345678")
                user.save()

            users.append(user)

        # =========================
        # Cinemas
        # =========================

        cinemas = []

        for _ in range(cinemas_count):
            cinema = Cinema.objects.create(
                name=fake.company(),
                address=fake.address(),
            )

            cinemas.append(cinema)

        # =========================
        # Halls + Seats
        # =========================

        halls = []

        for cinema in cinemas:
            for hall_number in range(halls_count):
                hall = Hall.objects.create(
                    cinema=cinema,
                    name=f"Hall {hall_number + 1}",
                    capacity=50,
                )

                halls.append(hall)

                for row in ["A", "B", "C", "D", "E"]:
                    for number in range(1, 11):
                        Seat.objects.create(
                            hall=hall,
                            row=row,
                            number=number,
                        )

        # =========================
        # Movies
        # =========================

        movies = []

        genres = [
            "Action",
            "Drama",
            "Comedy",
            "Sci-Fi",
            "Horror",
            "Thriller",
        ]

        age_ratings = [
            "G",
            "PG",
            "PG-13",
            "R",
        ]

        for _ in range(movies_count):
            movie = Movie.objects.create(
                title=fake.unique.sentence(nb_words=3).replace(".", ""),
                description=fake.paragraph(nb_sentences=5),
                release_date=fake.date_between(
                    start_date="-10y",
                    end_date="today",
                ),
                duration=random.randint(80, 180),
                genre=random.choice(genres),
                age_rating=random.choice(age_ratings),
            )

            movies.append(movie)

        # =========================
        # Showtimes
        # =========================

        showtimes = []

        for movie in movies:
            selected_halls = random.sample(
                halls,
                min(3, len(halls)),
            )

            for hall in selected_halls:
                start_time = timezone.now() + timedelta(
                    days=random.randint(1, 30),
                    hours=random.randint(0, 8),
                )

                end_time = start_time + timedelta(
                    minutes=movie.duration,
                )

                showtime = Showtime.objects.create(
                    movie=movie,
                    hall=hall,
                    start_time=start_time,
                    end_time=end_time,
                    price=Decimal(
                        random.choice(
                            [
                                "120000.00",
                                "150000.00",
                                "180000.00",
                                "200000.00",
                            ]
                        )
                    ),
                )

                showtimes.append(showtime)

        # =========================
        # Reservations
        # =========================

        reservation_count = 0

        for _ in range(reservations_count):
            showtime = random.choice(showtimes)

            available_seats = list(
                Seat.objects.filter(
                    hall=showtime.hall
                ).exclude(
                    reservations__showtime=showtime
                )
            )

            if not available_seats:
                continue

            seat = random.choice(available_seats)
            user = random.choice(users)

            Reservation.objects.create(
                user=user,
                showtime=showtime,
                seat=seat,
                status=random.choice(
                    [
                        Reservation.StatusChoices.PENDING,
                        Reservation.StatusChoices.CONFIRMED,
                        Reservation.StatusChoices.CANCELLED,
                    ]
                ),
            )

            reservation_count += 1

        # =========================
        # Result
        # =========================

        self.stdout.write(
            self.style.SUCCESS(
                "Fake data created successfully!"
            )
        )

        self.stdout.write(
            f"Users: {users_count}"
        )

        self.stdout.write(
            f"Movies: {movies_count}"
        )

        self.stdout.write(
            f"Cinemas: {cinemas_count}"
        )

        self.stdout.write(
            f"Halls: {len(halls)}"
        )

        self.stdout.write(
            f"Reservations: {reservation_count}"
        )
