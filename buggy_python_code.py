# contains bunch of buggy examples
import subprocess
import base64
import flask

# Input injection
def transcode_file(request, filename):
    command = 'ffmpeg -i "{source}" output_file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def food(request, user):
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh(object):
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))

def import_urlib_version(version):
    exec("import urllib%s as urllib" % version)

@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
