posts = []

def create_post():
    post = {
        "title": input("Enter title: "),
        "content": input("Enter content: "),
        "author": input("Enter author: ")
    }

    posts.append(post)
    print("Post created successfully.")


def view_posts():
    for post in posts:
        print("\nTitle:", post["title"])
        print("Author:", post["author"])
        print("Content:", post["content"])


create_post()
view_posts()
