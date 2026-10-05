posts = []

def create_post():
    post = {
        "title": input("Title: "),
        "content": input("Content: "),
        "status": "Pending"
    }

    posts.append(post)
    print("Post submitted for moderation.")


def moderate_posts():
    for post in posts:
        print("\nTitle:", post["title"])
        print("Status:", post["status"])

        choice = input("Approve this post? (y/n): ")

        if choice.lower() == "y":
            post["status"] = "Approved"
        else:
            post["status"] = "Rejected"

    print("Moderation completed.")


def view_approved_posts():
    print("\n===== APPROVED POSTS =====")

    for post in posts:
        if post["status"] == "Approved":
            print("\nTitle:", post["title"])
            print("Content:", post["content"])


create_post()
moderate_posts()
view_approved_posts()
