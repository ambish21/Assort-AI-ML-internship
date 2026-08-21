from database import students_collection


def insert_student(student):
    result = students_collection.insert_one(student)
    return result.inserted_id


def insert_students(students):
    result = students_collection.insert_many(students)
    return result.inserted_ids


def get_students():
    return list(students_collection.find())


def update_student(name, new_marks):
    result = students_collection.update_one(
        {"name": name},
        {"$set": {"marks": new_marks}}
    )
    return result.modified_count


def update_students_by_course(course):
    result = students_collection.update_many(
        {"course": course},
        {"$set": {"status": "Active"}}
    )
    return result.modified_count


def delete_student(name):
    result = students_collection.delete_one(
        {"name": name}
    )
    return result.deleted_count


def delete_students_by_marks():
    result = students_collection.delete_many(
        {"marks": {"$lt": 40}}
    )
    return result.deleted_count