import mysql.connector

class DatabaseHandler:
    def __init__(self):
        self.conn = mysql.connector.connect(
    host='db',  # Use the service name defined in docker-compose.yml
    user='root',
    password='password',  # Replace with your actual password
    database='notedb'
)

        self.cursor = self.conn.cursor(dictionary=True)

    def get_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        return self.cursor.fetchall()

    
    def create_note(self, title, content):
        try:
            self.cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error creating note: {e}")
            return False

    def update_note(self, note_id, title=None, content=None):
        try:
            query = "UPDATE notes SET "
            params = []
            if title:
                query += "title = %s, "
                params.append(title)
            if content:
                query += "content = %s "
                params.append(content)
            query = query.rstrip(', ')
            query += "WHERE id = %s"
            params.append(note_id)
            
            self.cursor.execute(query, tuple(params))
            if self.cursor.rowcount > 0:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error updating note: {e}")
            return False

    def delete_note(self, note_id):
        try:
            self.cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
            if self.cursor.rowcount > 0:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error deleting note: {e}")
            return False
