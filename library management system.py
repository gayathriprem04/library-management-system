from datetime import datetime, timedelta

library = []
members = []
transactions = []
fines = []

def add_book(book_id, title, copies):
    library.append({"id": book_id, "title": title, "copies": copies})

def add_member(member_id, name):
    members.append({"id": member_id, "name": name})

def issue_book(transaction_id, book_id, member_id):
    for book in library:
        if book["id"] == book_id:
            if book["copies"] > 0:
                book["copies"] -= 1
                due_date = datetime.now() + timedelta(days=7)
                transactions.append({
                    "id": transaction_id,
                    "book_id": book_id,
                    "member_id": member_id,
                    "due_date": due_date,
                    "status": "Issued"
                })
                print(f"Issued '{book['title']}' (Due: {due_date.date()})")
                return

def return_book(transaction_id):
    for txn in transactions:
        if txn["id"] == transaction_id and txn["status"] == "Issued":
            txn["status"] = "Returned"
            for book in library:
                if book["id"] == txn["book_id"]:
                    book["copies"] += 1
            if datetime.now() > txn["due_date"]:
                days_late = (datetime.now() - txn["due_date"]).days
                fine_amount = days_late * 10
                fines.append({"transaction_id": transaction_id, "member_id": txn["member_id"], "amount": fine_amount})
                print(f"Returned late by {days_late} days. Fine ₹{fine_amount}")
            else:
                print("Returned on time")
            return

def show_fines():
    if not fines:
        print("No fines")
        return
    for fine in fines:
        print(f"Transaction {fine['transaction_id']} - Fine ₹{fine['amount']}")

# Demo
add_book(1, "Python Basics", 3)
add_member(1, "Gayathri")
issue_book(1, 1, 1)
transactions[0]["due_date"] = datetime.now() - timedelta(days=3)
return_book(1)
show_fines()