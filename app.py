from flask import Flask, request, Response
import gzip
import io
import os

app = Flask(__name__)

@app.route('/decompress', methods=['POST'])
def decompress_gz():
    try:
        # Get raw gzip file from request body
        raw_gz = request.get_data()
        
        # Decompress
        decompressed_xml = gzip.decompress(raw_gz).decode('utf-8')

        return Response(decompressed_xml, mimetype='text/xml')

    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
