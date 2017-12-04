<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
	<header><h1>Categories</h1></header>
	<nav>
	<form method="get" action="/sell">
	    <button type="submit">Sell</button>
	</form>
	</nav>
	<main>
	%try:
	%for value in categories:
	%for v in value:
	<a href="/{{v}}">{{v}}</a><br>
	%end
	%end
	%except NameError:
	<h3>No categories yet</h3>
	%end
	</main>
</body>
</html>
