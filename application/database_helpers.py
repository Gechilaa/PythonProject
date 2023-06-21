def create_users_table(db):
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS USERS
        (
            ID INTEGER PRIMARY KEY AUTOINCREMENT ,
            FIRST_NAME TEXT(50) NOT NULL ,
            LAST_NAME TEXT(50) NOT NULL ,
            BIRTH_DATE TEXT(50) NOT NULL ,
            PHONE_NUMBER TEXT(50) NOT NULL ,
            EMAIL TEXT(50) NOT NULL ,
            PASSWORD TEXT(50) NOT NULL 
        )
        '''
    )


def add_new_user(db, first_name, last_name, birth_date, phone, email, password):
    cursor = db.cursor()
    cursor.execute(
        '''
        INSERT INTO USERS (FIRST_NAME, LAST_NAME, BIRTH_DATE, PHONE_NUMBER, EMAIL, PASSWORD)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, birth_date, phone, email, password)
    )
    db.commit()


def get_all_users(db, email, password):
    cursor = db.cursor()
    cursor.execute(
        '''
        SELECT * FROM USERS WHERE EMAIL=? AND PASSWORD=?
        ''', (email, password)
    )
    return cursor.fetchone()