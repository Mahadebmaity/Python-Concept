comment = input("Enter a comment: ")
comment_lower = comment.lower() 
if "make a lot of money" in comment_lower or "buy now!" in comment_lower or "subscribe this" in comment_lower or "click this link" in comment_lower:
    print("This is spam comment.") 
else:
    print("This is not spam comment.")

# question 2 
username = input("Enter your username: ")
lenth = len(username)
if lenth < 10:
    print("Username contains less than 10 characters.")
else:
    print("Almost there, your username is good to go!")


