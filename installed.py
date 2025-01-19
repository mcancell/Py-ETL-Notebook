import pkg_resources

def list_installed_packages():
    installed_packages = pkg_resources.working_set
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
    for package in installed_packages_list:
        print(package)

if __name__ == "__main__":
    list_installed_packages()