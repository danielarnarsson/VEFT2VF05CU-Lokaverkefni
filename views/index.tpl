<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
	<div>
		<h1>Categories</h1>
		%try:
		%for value in categories:
		%for v in value:
		<a href="/{{v}}">{{v}}</a><br>
		%end
		%end
		%except NameError:
		<h3>No categories yet</h3>
		%end
	</div>
	<form method="get" action="/sell">
	    <button type="submit">Sell</button>
	</form>
</body>
</html>