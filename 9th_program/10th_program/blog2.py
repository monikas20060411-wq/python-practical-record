posts = []

def create_post():
    post = {
        "id": len(posts) + 1,
        "title": input("Title: "),
        "content": input("Content: ")
    }

    posts.append(post)
    print("Post added.")


def edit_post():
    post_id = int(input("Enter post ID: "))

    for post in posts:
        if post["id"] == post_id:
            post["title"] = input("New title: ")
            post["content"] = input("New content: ")

            print("Post updated.")
            return

    print("Post not found.")


def view_posts():
    for post in posts:
        print("\nID:", post["id"])
        print("Title:", post["title"])
        print("Content:", post["content"])


create_post()
view_posts()
edit_post()
view_posts()
