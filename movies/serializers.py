from rest_framework import serializers
from movies.models import Movie, MovieRating, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        choices=MovieRating.choices, default=MovieRating.DEFAULT
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127, source="movie.title", read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.EmailField(source="user.email", read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
