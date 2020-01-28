from setuptools import setup

setup(
    name="girder-ess-dive",
    version="1.0.0",
    description="Allows access to ESS-DIVE files through a read-only assetstore.",
    packages=["girder_ess_dive"],
    install_requires=[
        "girder",
        "pytest",
        "requests",
        "xmltodict",
        "shapely",
        "pyproj",
    ],
    entry_points={"girder.plugin": ["ess-dive = girder_ess_dive:GirderESSDive"]},
)
