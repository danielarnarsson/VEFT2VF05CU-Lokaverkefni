<html>
<head>
	<link type="text/css" href="/static/css/styles.css" rel="stylesheet">
</head>
<body>
%for value in products:
%x=0
%for v in value:
%x=x+1
%if x == 1:
<h3>{{v}}</h3>
%elif x == 2:
<p>Verð: {{v}} kr</p>
%elif x == 3:
<p>Upplýsingar:</p>
<p>{{v}}</p>
%end
%end
</body>
</html>