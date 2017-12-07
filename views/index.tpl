<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
<header><h1>Categories</h1></header>
	<main>
	%if len(categories) == 0:
	<br>
	<h3>No categories yet</h3>
	%else:
		%for value in categories:
			%for v in value:
				<a href="/{{v}}">{{v}}</a><br>
		%end
	%end
	</main>
	<nav>
	<form method="get" action="/sell">
	    <button type="submit">Sell</button>
	</form>
	</nav>
</body>
</html>
