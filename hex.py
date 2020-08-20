import random
import string
import cherrypy

class HexaDecimal(object):
	@cherrypy.expose
	def index(self):
		return """<!doctype html>
		<html lang="en">
		<!-- Required meta tags -->
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
		<!-- Bootstrap CSS -->
		<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
		<title>HexaDecimal</title>
		</head>
		<body>
		<h1><p><a href="generate" class="btn btn-primary">Generate</a></p></h1>
		<!-- Optional JavaScript -->
		<!-- jQuery first, then Popper.js, then Bootstrap JS -->
		<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
		<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
		</html>"""

	@cherrypy.expose
	def generate(self, length=8):
		return ''.join(random.sample(string.hexdigits, int(length)))

if __name__ == '__main__':
	cherrypy.quickstart(HexaDecimal())