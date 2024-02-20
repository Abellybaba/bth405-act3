from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs
from database_handler import DatabaseHandler


class RequestHandler(BaseHTTPRequestHandler):
    db_handler = DatabaseHandler()

    def _send_response(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.path.startswith('/notes'):
            notes = self.db_handler.get_notes()
            self._send_response(200, notes)
        else:
            self._send_response(404, {'message': 'Not Found'})
            

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        note_data = json.loads(post_data)
        
        if self.path == '/notes':
            success = self.db_handler.create_note(note_data['title'], note_data['content'])
            if success:
                self._send_response(201, {'message': 'Note created'})
            else:
                self._send_response(500, {'message': 'Internal Server Error'})
        else:
            self._send_response(404, {'message': 'Not Found'})
            
        
    
    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        note_data = json.loads(put_data)
        note_id = self.path.split('/')[-1]

        success = self.db_handler.update_note(note_id, note_data.get('title'), note_data.get('content'))
        if success:
            self._send_response(200, {'message': 'Note updated'})
        else:
            self._send_response(404, {'message': 'Note not found'})

    def do_DELETE(self):
        note_id = self.path.split('/')[-1]
        success = self.db_handler.delete_note(note_id)
        if success:
            self._send_response(200, {'message': 'Note deleted'})
        else:
            self._send_response(404, {'message': 'Note not found'})
            
            

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd server..')

if __name__ == '__main__':
    run()

   
   
   
    

    
