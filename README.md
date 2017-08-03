# plaxedpy
Social Network based on Django / Python specifically for gamers.
<h2>Requirements</h2>
<ol>
    <li>Python 3 (Im using Python 3.5.2 in Ubuntu Gnome, tested in Linux, not tested in Windows.)</li>
</ol>

<h2>Installation</h2>
<ol>
    <li><code>git pull https://github.com/cotizcesar/plaxedpy.git</code></li>
    <li><code>cd plaxedpy</code></li>
    <li><code>python3 -m venv venv</code></li>
    <li><code>source venv/bin/activate</code></li>
    <li><code>pip install -r requirements.txt</code></li>
    <li><code>python manage.py migrate</code></li>
    <li><code>python manage.py createsuperuser</code></li>
    <li><code>export SECRET_KEY='put a secret key here.'</code></li>
    <li><code>python manage.py runserver</code></li>
    <li>Go to <code>http://127.0.0.1/admin/</code> and user your login and password. Go to "Site" section <code>http://127.0.0.1/admin/sites/site/add/</code>and put a Domain name and a Display Name.</li>
    <li>Activate your Social Network API's (Battle.net, Facebook, Discord and Twitch) here <code>http://127.0.0.1/admin/socialaccount/socialapp/</code></li>
    <li>... and you are ready to GO!</li>
</ol>