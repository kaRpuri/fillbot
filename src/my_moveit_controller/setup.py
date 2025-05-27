from setuptools import find_packages, setup

package_name = 'my_moveit_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    entry_points={
        'console_scripts': [
            'move_to_pose = my_moveit_controller.scripts.moveit_control:main',  # Single entry point
        ],
    },
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kabirpuri',
    maintainer_email='kapuri@seas.upenn.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
)
