import psycopg2





class Student:
    def __init__(self, name, gender, unit, father_name, mother_name, father_phone_number, mother_phone_number, father_job, mother_job, student_phone, birth_place, birth_date, joining_date, address, grade, tuition_fee):
        self.name = name
        self.gender = gender
        self.unit = unit
        self.father_name = father_name
        self.mother_name = mother_name
        self.father_phone_number = father_phone_number
        self.mother_phone_number = mother_phone_number
        self.father_job = father_job
        self.mother_job = mother_job
        self.student_phone = student_phone
        self.birth_place = birth_place
        self.birth_date = birth_date
        self.joining_date = joining_date
        self.address = address
        self.grade = grade
        self.tuition_fee = tuition_fee

    @staticmethod
    def add_student_to_db(student):
        # establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="school_db",
            user="postgres",
            password="adeeb"
                )
        
        # create a cursor  object to execute SQL queries
        cur = conn.cursor()
        query = '''INSERT INTO students (
                       name, gender, unit, father_name, mother_name, father_phone_number, mother_phone_number,
                       father_job, mother_job, student_phone, birth_place, birth_date, joining_date, address,
                       grade, tuition_fee
                   )
                   VALUES (
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                   );'''
        values = (
            student.name, student.gender, student.unit, student.father_name, student.mother_name,
            student.father_phone_number, student.mother_phone_number, student.father_job, student.mother_job,
            student.student_phone, student.birth_place, student.birth_date, student.joining_date, student.address,
            student.grade, student.tuition_fee
        )
        try:
            cur.execute(query, values)
            conn.commit()
            print("Insert query executed successfully")
            cur.close()
            conn.close()
            return True
        except psycopg2.Error as e:
            print(f"Error inserting data: {e}")
            cur.close()
            conn.close()
            return False
            
        
            

        

    @staticmethod
    def remove(student_id):
        # establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="school_db",
            user="postgres",
            password="adeeb"
        )
        
        # create a cursor object to execute SQL queries
        cur = conn.cursor()
        query = '''DELETE FROM students WHERE id = %s;'''
        cur.execute(query, (student_id,))
        conn.commit()

    @staticmethod
    def edit(student_id, field, value):
        # establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="school_db",
            user="postgres",
            password="adeeb"
        )
        
        # create a cursor object to execute SQL queries
        cur = conn.cursor()


        query = f'''UPDATE students SET {field} = %s WHERE id = %s;'''
        cur.execute(query, (value, student_id))

    
    @staticmethod
    def update_in_db(student, student_id):

        conn = psycopg2.connect(
            host="127.0.0.1",
            database="school_db",
            user="postgres",
            password="adeeb"
        )
        
        # create a cursor object to execute SQL queries
        cur = conn.cursor()
        student_id=int(student_id)
        # Prepare the SQL statement to update the student in the database.
        query = '''
            UPDATE students SET
                name = %s,
                gender = %s,
                unit = %s,
                father_name = %s,
                mother_name = %s,
                father_phone_number = %s,
                mother_phone_number = %s,
                father_job = %s,
                mother_job = %s,
                student_phone = %s,
                birth_place = %s,
                birth_date = %s,
                joining_date = %s,
                address = %s,
                grade = %s,
                tuition_fee = %s
            WHERE id = %s
        '''
        values = (
            student.name, student.gender, student.unit, student.father_name, student.mother_name, student.father_phone_number,
            student.mother_phone_number, student.father_job, student.mother_job, student.student_phone, student.birth_place,
            student.birth_date, student.joining_date, student.address, student.grade, student.tuition_fee, student_id
        )

        # Execute the SQL statement to update the student in the database.
        cur.execute(query, values)
        conn.commit()

    
    
    
    @staticmethod
    def get_student_by_id(student_id):
        # establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="school_db",
            user="postgres",
            password="adeeb"
        )
        
        # create a cursor object to execute SQL queries
        cur = conn.cursor()
        
        query = '''SELECT * FROM students WHERE id = %s;'''
        values = (student_id,)
        
        try:
            cur.execute(query, values)
            student_data = cur.fetchone()
            if student_data:
                student_data= student_data[1:]
            
            if student_data:
                student = Student(*student_data)
                return student
            else:
                print(f"No student found with id {student_id}")
                return None
        except psycopg2.Error as e:
            print(f"Error retrieving data: {e}")
            return None
        finally:
            cur.close()
            conn.close()
    
