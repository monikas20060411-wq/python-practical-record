posts = []

def create_post():
    post = {
        "id": len(posts) + 1,
        "title": input("Title: "),
        "content": input("Content: "),
        "comments": [],
        "status": "Pending"
    }

    posts.append(post)

    print("Post created successfully.")


def view_posts():
    print("\n===== BLOG POSTS =====")

    for post in posts:
        if post["status"] == "Approved":
            print("\nID:", post["id"])
            print("Title:", post["title"])
            print("Content:", post["content"])

            print("Comments:")
            for comment in post["comments"]:
                print("-", comment)


def edit_post():
    post_id = int(input("Enter post ID: "))

    for post in posts:
        if post["id"] == post_id:
            post["title"] = input("New title: ")
            post["content"] = input("New content: ")
            post["status"] = "Pending"

            print("Post updated and sent for moderation.")
            return

    print("Post not found.")


def add_comment():
    post_id = int(input("Enter post ID: "))

    for post in posts:
        if post["id"] == post_id:

            if post["status"] != "Approved":
                print("Comments are allowed only on approved posts.")
                return

            comment = input("Enter comment: ")
            post["comments"].append(comment)

            print("Comment added.")
            return

    print("Post not found.")


def moderate_posts():
    for post in posts:

        if post["status"] == "Pending":

            print("\nPost ID:", post["id"])
            print("Title:", post["title"])
            print("Content:", post["content"])

            choice = input("Approve post? (y/n): ")

            if choice.lower() == "y":
                post["status"] = "Approved"
                print("Post approved.")

            else:
                post["status"] = "Rejected"
                print("Post rejected.")


def delete_post():
    post_id = int(input("Enter post ID: "))

    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)
            print("Post deleted.")
            return

    print("Post not found.")


# Main menu
while True:

    print("\n===== BLOG MANAGEMENT SYSTEM =====")
    print("1. Create Post")
    print("2. View Posts")
    print("3. Edit Post")
    print("4. Add Comment")
    print("5. Admin Moderation")
    print("6. Delete Post")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create_post()

    elif choice == "2":
        view_posts()

    elif choice == "3":
        edit_post()

    elif choice == "4":
        add_comment()

    elif choice == "5":
        moderate_posts()

    elif choice == "6":
        delete_post()

    elif choice == "7":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
