from instapy import InstaPy

#session = InstaPy(username="ellis_from_los", password="Ellisfromlos1", headless_browser=True)
session = InstaPy(username="kasianova_production", password="Ellisfromlos12", headless_browser=True, nogui=True)
#session = InstaPy(username="8stones_marble_showroom8", password="8stones8stones", headless_browser=True)
session.login()

#session.set_dont_like(["naked", "nsfw"])
#session.set_do_follow(True, percentage=50)
session.set_do_follow(enabled=False, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Perfect!"])
session.set_skip_users(skip_private=True,
                   private_percentage=100,
                   skip_business=True,
                   skip_non_business=False,
                   business_percentage=100)
session.set_relationship_bounds(enabled=True, max_followers=1000)

# It should be at the end of this file
session.like_by_tags(["flatlays","winterflatlay","cozyhome","winterstories","snow","photooftheday","picsoftheday"], amount=31)
#session.like_by_tags(["marble","luxury","luxurylifestyle","girls","nightlife","photooftheday","kyivgramm"], amount=11)
session.end()
