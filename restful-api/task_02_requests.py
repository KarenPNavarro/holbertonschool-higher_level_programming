#!/usr/bin/python3
"""Module that fetches and processes posts from JSONPlaceholder API."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts and print their titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save them to a CSV file."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()
        rows = [{"id": p["id"], "title": p["title"], "body": p["body"]}
                for p in posts]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
