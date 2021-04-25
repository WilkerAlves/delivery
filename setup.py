from setuptools import setup, find_packages


def read(filename):
    return [
        req.strip() 
        for req 
        in open(filename).readlines()
    ]


setup(
    name="delivery",
    version="0.1.0", #major (mudança grande), minor (versão propriamente dita), path (corrções)
    description="Projeto do curso de flask DELIVERY APP",
    packages=find_packages(exclude=".venv"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require ={"dev": read("requirements-dev.txt")}
)



# instalar o projeto de forma editavel pip install -e .
# esse ponto para ele procurar o setup.py na raiz