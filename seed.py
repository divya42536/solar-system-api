from app import create_app, db
from app.models.Moons import Moons
from app.models.Planets import Planets
from dotenv import load_dotenv

moons = [
    {
        "name": "Moon1",
       "Planets": [
            {"name": "Earth"},
            {"description": "The only known planet with life and abundant water"},
            {"atmosphere": "Nitrogen and Oxygen"},
    
        ],
},
{
  
      "name": "Moon2",
      "Planets": [
            {"name": "Mars"},
            {"description": "Known as the Red Planet with dusty landscapes and iron oxide"},
            {"atmosphere": "Carbon Dioxide"},
      ],
  },
]

loaners = [
    {"name": "planet1", "description": "white", "atmosphere": "floats through life"},
    {"name": "planet2", "description": "calico", "atmosphere": "always in the details"},
    {"name": "planet3", "description": "silver", "atmosphere": "runs like the wind"},
]


def get_model_by_field(cls, data_dict, key_name):
    value = data_dict[key_name]
    stmt = db.select(cls).where(getattr(cls, key_name) == value)
    return db.session.scalar(stmt)

load_dotenv()
my_app = create_app()
with my_app.app_context():

    for moon_data in moons:
        Moon = get_model_by_field(moons, moon_data, "name")
        if not Moon:
            Moon = Moons(name=moon_data["name"])
            db.session.add(Moon)
            db.session.flush()  

        for planet_data in moon_data["Planets"]:
            planet = get_model_by_field(Moon, moon_data, "name")
            if not Moon:
                Moon = Moons(
                    name=moon_data["name"],
                    description=moon_data["description"],
                    atmosphere=moon_data["atmosphere"],
                    Moon_id=Moon.id
                )
                db.session.add(planet)

   
    for planet_data in loaners:
        planet = get_model_by_field(Planets, planet_data, "name")
        if not planet:
            planet = Planets(
                name=planet_data["name"],
                description=planet_data["description"],
                atmosphere=planet_data["atmosphere"],
                moon_id=None
            )
            db.session.add(planet)

    db.session.commit()