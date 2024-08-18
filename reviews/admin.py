from django.contrib import admin
from .models import Review


class RatingFilter(admin.SimpleListFilter):

    title = "Filter by rating!"

    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        rating = self.value()
        if rating:
            if rating == "good":
                return reviews.filter(rating__gte=3)
            else:
                return reviews.filter(rating__lt=3)
        return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        RatingFilter,
        "rating",)
