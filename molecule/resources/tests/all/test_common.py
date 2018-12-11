
debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_install_dir(host):
    f = host.file('/opt/redis_exporter')

    assert f.exists
    assert f.is_directory


def test_config_file(host):
    f = host.file('/opt/redis_exporter/shared/config')

    assert f.exists
    assert f.is_file


def test_release_dir(host):
    f = host.file('/opt/redis_exporter/releases/0.23.0')

    assert f.exists
    assert f.is_directory


def test_release_symlink_dir(host):
    f = host.file('/opt/redis_exporter/current')

    assert f.exists
    assert f.is_symlink
    assert f.linked_to == '/opt/redis_exporter/releases/0.23.0'


def test_service(host):
    s = host.service('redis_exporter')

    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket('tcp://0.0.0.0:9121')

    assert s.is_listening


def test_user(host):
    u = host.user('redis-exp')

    assert u.shell == '/usr/sbin/nologin'


def test_group(host):
    g = host.user('redis-exp')

    assert g.exists
