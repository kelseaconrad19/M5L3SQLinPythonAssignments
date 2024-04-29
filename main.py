import mysql.connector
from mysql.connector import Error

db_name = 'gym_database'
user = 'root'
password = 'jeweller-zipper-reck2'
host = '127.0.0.1'


def add_member(id, name, age, trainer_id):
    """Takes the member's id, name, age, and trainer's name and adds a new member to the Members table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        new_member = (id, name, age, trainer_id)
        # Query to insert a new member into the Members table
        query = 'INSERT INTO Members (id, name, age, trainer_id) VALUES (%s, %s, %s, %s)'
        # Execute the query with the new member parameters
        cursor.execute(query, new_member)
        conn.commit()
        print('New member added')
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


def add_workout_session(member_id, session_date, duration_minutes, calories_burned):
    """Takes the member's id, session date, duration in minutes, and calories burned and adds a new workout session to the WorkoutSessions table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        new_workout_session = (member_id, session_date, duration_minutes, calories_burned)
        # Query to insert a new workout session into the WorkoutSessions table
        query = 'INSERT INTO WorkoutSessions (member_id, session_date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)'
        # Execute the query with the new workout session parameters
        cursor.execute(query, new_workout_session)
        conn.commit()
        print('New workout session added')
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


def update_member_age(id, new_age):
    """Takes the member's id and new age and updates the age of the member in the Members table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        member_id = (id,)
        # Query to select a member by id - Used to check if the member exists
        query = 'SELECT * FROM Members WHERE id = %s'

        # check if member_id exists
        cursor.execute(query, member_id)
        if not cursor.fetchone():
            print('Member does not exist')
            return
        else:
            new_info = (new_age, id)
            # Query to update the age of a member by id
            query = 'UPDATE Members SET age = %s WHERE id = %s'
            # Execute the query with the new age and member id parameters
            cursor.execute(query, new_info)
            conn.commit()
            print('Member age updated')
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


def delete_workout_session(id):
    """Takes the workout session id and deletes the workout session from the WorkoutSessions table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        session_id = (id,)
        # Query to select a workout session by id - Used to check if the session exists
        query = 'SELECT * FROM WorkoutSessions WHERE id = %s'
        # Execute the query with the session id parameter
        cursor.execute(query, session_id)
        # Check if the workout session exists
        if not cursor.fetchone():
            print('Workout session does not exist')
            return
        else:
            # Query to delete a workout session by id
            query = 'DELETE FROM WorkoutSessions WHERE id = %s'
            # Execute the query with the session id parameter
            cursor.execute(query, session_id)
            # Commit the changes
            conn.commit()
            print('Workout session deleted')
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


def list_distint_trainers():
    """Lists the distinct trainers from the Members table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        # Query to select distinct trainers from the Members table
        query = 'SELECT DISTINCT trainer_id FROM Members'
        # Execute the query
        cursor.execute(query)
        # Fetch all the distinct trainers
        trainers = cursor.fetchall()
        print('Distinct trainers:')
        # Print the distinct trainers
        for trainer in trainers:
            print(trainer[0])
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


def count_members_per_trainer():
    """Counts the number of members per trainer from the Members table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        # Query to count the number of members per trainer
        query = 'SELECT trainer_id, COUNT(*) FROM Members GROUP BY trainer_id'
        # Execute the query
        cursor.execute(query)
        # Fetch all the trainers and the count of members per trainer
        members_per_trainer = cursor.fetchall()
        print('Members per trainer:')
        # Print the trainer and the count of members per trainer
        for trainer, count in members_per_trainer:
            print(f'Trainer {trainer}: {count} members')
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


def get_members_in_age_range(start_age, end_age):
    """Takes a start age and an end age and returns the members whose age falls within the specified range from the Members table in the database."""
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            password=password,
            host=host
        )
        cursor = conn.cursor()

        age_range = (start_age, end_age)
        # Query to select members whose age falls within the specified range
        query = 'SELECT * FROM Members WHERE age BETWEEN %s AND %s'
        # Execute the query with the age range parameters
        cursor.execute(query, age_range)
        # Fetch all the members whose age falls within the specified range
        members = cursor.fetchall()
        print('Members in age range:')
        # Print the members whose age falls within the specified range
        for member in members:
            print(member)
    except Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()
        conn.close()
        print('Connection closed')


if __name__ == '__main__':
    # add_member(1, 'Alice', 30, 2)
    # add_member(2, 'Charlie', 25, 4)
    # add_member(3, 'Eve', 35, 4)
    #
    # add_workout_session(4, '2021-01-01', 60, 300)
    # add_workout_session(3, '2021-01-02', 45, 250)
    # add_workout_session(2, '2021-01-01', 30, 150)
    #
    # update_member_age(4, 31)
    # update_member_age(2, 26)
    # update_member_age(3, 36)
    #
    # delete_workout_session(8)

    list_distint_trainers()
    count_members_per_trainer()
    get_members_in_age_range(25, 30)
