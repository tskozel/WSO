VERIFICATION_TEMPLATE = """
<h1>Hi {{ first_name }},</h1>
<p>
    in order to use our services, please click the link below:
    <br>
    <a href="{{ url_for('stats.overview', token=token, _external=True) }}">verify email</a>
</p>
<p>If you did not create an account, you may ignore this message.</p>
"""
