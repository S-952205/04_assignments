# iss program main humein apna weight mars pay calculate krna hai mars pay gravity kmm hoti hai
# gravity on mars = 37.8% (0.378) yani agar earth pay hamara weight 100kg hai tw mars pay 37 hoga humein apna
# earth pay jo weight hai woo dena hai


MARS_GRAV: float = 0.378


def mars_weight():
    

        earth_weight: float = float(input('Enter a weight one earth: '))

        mars_weight: float = earth_weight * MARS_GRAV
        rounded_weight: float = round(mars_weight, 2)

        print(rounded_weight)



if __name__ == '__main__':
    mars_weight()