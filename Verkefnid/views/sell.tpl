<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
<div>
<h1>Skráning</h1>
<a></a>
</div>
<form method="post" action="/sell">
	<br>
	<b>Titill</b>
	<br>
	<input type="text" name="title">
	<br>
	<br>
	<b>Mynd</b>
	<br>
	<input type="file" accept="image/jpeg,image/png">
	<br>
	<br>
	<b>Verð</b>
	<br>
	<input type="number" name='price'><b> kr</b>
	<br>
	<br>
	<b>Upplýsingar</b>
	<br>
	<textarea name="info" rows=10 cols=50 maxlength=1000></textarea>
	<br>
	<br>
<input type="submit">
</form>
%if saved == True:
<h2>Vara vistuð.</h2>
<a href="/">Til baka</a>
%end
</body>
</html>