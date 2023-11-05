from sonar import Sonar



if __name__ == '__main__':
    sonar = Sonar()
    print(sonar.web_server_address)

    print(sonar.set_volume("master", 1))
