

class Exam:
    def __init__(self, student_id, exam_date, subject, score):
        self.student_id = student_id
        self.exam_date = exam_date
        self.subject = subject
        self.score = score

    def save_to_db(self, db):
        db.execute("INSERT INTO exams (student_id, exam_date, subject, score) VALUES (%s, %s, %s, %s);",
                   (self.student_id, self.exam_date, self.subject, self.score))

    @classmethod
    def get_by_student_id(cls, db, student_id):
        db.execute("SELECT * FROM exams WHERE student_id = %s;", (student_id,))
        rows = db.fetchall()
        return [cls(*row) for row in rows]

    @classmethod
    def get_all(cls, db):
        db.execute("SELECT * FROM exams;")
        rows = db.fetchall()
        return [cls(*row) for row in rows]
    
    def __repr__(self):
        return f"Exam(student_id={self.student_id}, exam_date={self.exam_date}, subject={self.subject}, score={self.score})"
