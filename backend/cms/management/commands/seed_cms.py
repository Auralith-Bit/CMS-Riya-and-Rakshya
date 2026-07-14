from django.core.management.base import BaseCommand

from cms.models import Category, ContactInfo, Feedback, HomePageContent


class Command(BaseCommand):
    help = "Create starter CMS records for R&R Food Products."

    def handle(self, *args, **options):
        categories = [
            "Spicy Namkeen",
            "Bhujha & Chatpate Bhujha",
            "Fryums",
            "Chips/Kurkure/Cheese Balls",
            "Puffs",
            "Diet & Health",
        ]
        for index, name in enumerate(categories, start=1):
            Category.objects.get_or_create(
                name=name,
                defaults={
                    "description": "Crunchy, flavourful, and irresistible.",
                    "sort_order": index,
                    "is_active": True,
                },
            )

        HomePageContent.objects.get_or_create(
            id=1,
            defaults={
                "badge_text": "Nepal ko Swad",
                "hero_title": "One Bite & You Won't Stop Craving",
                "hero_highlight": "Craving",
                "hero_subtitle": (
                    "Instant noodles, crunchy snacks, and bulk packs delivered straight to your door. "
                    "Freshness guaranteed in every bite."
                ),
            },
        )

        ContactInfo.objects.get_or_create(
            id=1,
            defaults={
                "customer_support_phone": "+977 982-0299711",
                "business_phone": "+977 985-7021032",
                "whatsapp_number": "9779857021032",
                "support_email": "Support@riyarakshya.com.np",
                "sales_email": "Sales@riyarakshya.com.np",
                "address": "S.No.-4, SugarMill, Bhairahwa, Rupandehi, Nepal",
                "business_hours": "Sun-Fri: 9:00 AM - 6:00 PM",
            },
        )

        feedbacks = [
            {"customer_name": "Prakash Bhatta",      "location": "Pokhara, Kaski",      "text": "Kushal All In One has the proper Nepali chatpate taste. The namkeen stays crunchy, the masala is balanced, and every packet feels fresh.", "rating": 5, "sort_order": 1},
            {"customer_name": "Ramesh Kumar Yadav",   "location": "Butwal, Rupandehi",   "text": "I keep R&R snacks in my shop because customers ask for them again. The packaging looks clean, the price is practical, and the quality is consistent.", "rating": 5, "sort_order": 2},
            {"customer_name": "Sita Devi Chaudhary",  "location": "Janakpur, Dhanusha",  "text": "The mixture namkeen tastes homemade but has professional finishing. It is spicy, crunchy, and perfect with tea for the whole family.", "rating": 5, "sort_order": 3},
            {"customer_name": "Dipesh Mahato",        "location": "Biratnagar, Morang",  "text": "Potato chips and kids snacks are always fresh when they arrive. Good crunch, strong flavour, and very reliable for our canteen orders.", "rating": 5, "sort_order": 4},
            {"customer_name": "Sabina Thapa",         "location": "Hetauda, Makwanpur",  "text": "R&R products have become regular snacks in our home. The taste feels local, the packets are hygienic, and the delivery is dependable.", "rating": 5, "sort_order": 5},
            {"customer_name": "Bikash Adhikari",      "location": "Bharatpur, Chitwan",  "text": "The Korean Hot & Spicy noodles sell very fast in our store. Customers like the bold masala and the packet quality looks trustworthy.", "rating": 5, "sort_order": 6},
            {"customer_name": "Mina Karki",           "location": "Nepalgunj, Banke",    "text": "I ordered namkeen for our office tea break and everyone liked it. The flavour is not flat, the crunch lasts, and the price is reasonable.", "rating": 5, "sort_order": 7},
            {"customer_name": "Puja Lamichhane",      "location": "Tansen, Palpa",       "text": "Jungle Janawar and Cheese Balls are favourites for children in our family. Fresh packets, nice taste, and no stale smell at all.", "rating": 5, "sort_order": 8},
            {"customer_name": "Amit Sah",             "location": "Birgunj, Parsa",      "text": "As a retailer, I appreciate that the products are consistent from carton to carton. R&R snacks are easy to recommend to regular customers.", "rating": 5, "sort_order": 9},
            {"customer_name": "Anita Gurung",         "location": "Dharan, Sunsari",     "text": "The diet mixture has a clean taste and feels lighter than many other snacks. It is perfect when guests come home for chiya.", "rating": 5, "sort_order": 10},
            {"customer_name": "Kiran Rai",            "location": "Ilam",                "text": "Chatpate Bhuja has a strong local flavour and the crunch is excellent. It reminds me of snacks we buy during travel, but cleaner packed.", "rating": 5, "sort_order": 11},
            {"customer_name": "Laxmi Poudel",         "location": "Damak, Jhapa",        "text": "We use R&R snacks for school canteen supply because the small packs move quickly. Children like the taste and parents trust the hygiene.", "rating": 5, "sort_order": 12},
            {"customer_name": "Roshan KC",            "location": "Dang",                "text": "The masala in the namkeen is balanced very well. It is spicy enough for Nepali taste but does not feel too heavy.", "rating": 5, "sort_order": 13},
            {"customer_name": "Manisha Shahi",        "location": "Surkhet",             "text": "A-One chips are crispy and the flavour coating is even. Every packet I opened had the same freshness and crunch.", "rating": 5, "sort_order": 14},
            {"customer_name": "Hari Prasad Nepal",    "location": "Kathmandu",           "text": "For wholesale orders, R&R has been dependable. Cartons arrive properly packed and customers recognize the taste now.", "rating": 5, "sort_order": 15},
            {"customer_name": "Nirmala Magar",        "location": "Baglung",             "text": "Boondi mixture is very good with tea. The texture is light, the spice is clean, and the packet quality feels premium.", "rating": 5, "sort_order": 16},
            {"customer_name": "Sanjay Tamang",        "location": "Bhaktapur",           "text": "My family liked the kids snacks because they are fun and tasty. The products feel fresh, not oily or stale.", "rating": 5, "sort_order": 17},
            {"customer_name": "Rekha Sharma",         "location": "Lalitpur",            "text": "The snack range has good variety for a small store. Customers can choose noodles, chips, namkeen, and kids snacks from one brand.", "rating": 5, "sort_order": 18},
        ]
        for fb in feedbacks:
            Feedback.objects.get_or_create(
                customer_name=fb["customer_name"],
                defaults={**fb, "is_visible": True},
            )

        self.stdout.write(self.style.SUCCESS("Starter CMS data is ready."))
