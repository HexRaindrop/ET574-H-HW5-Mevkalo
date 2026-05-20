def installer_main():
    import sys
    import subprocess

    def install(package):
        subprocess.check_call([sys.executable, "-m","pip","install",package])
    modules_that_we_need_to_instal = ["numpy","pandas","wxpython","matplotlib","ucimlrepo"]

    for i in modules_that_we_need_to_instal:
        install(i)
        print(f"{i} is installed")
    print(f"\n{'-'*8}done{'-'*8}\nthe following modueles were installed\n")
    for i in modules_that_we_need_to_instal:
        print(i)
    print('-'*20)

installer_main()
