<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
	<header><h1>Categories</h1></header>
	<main>
	%try:
	%if len(categories) == 0:
	<h3>No categories yet</h3>
	%end
	%for value in categories:
	%for v in value:
	<a href="/{{v}}">{{v}}</a><br>
	%end
	%end
	%except:
	%pass
	%end
	</main>
	<nav>
	<form method="get" action="/sell">
	    <button type="submit">Sell</button>
	</form>
	</nav>
</body>
</html>
