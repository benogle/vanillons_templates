try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='vanillons_templates',
    version='0.0.1',
    description='Vanillons Templates',
    author='Ben Ogle',
    author_email='human@benogle.com',
    url='http://github.com/benogle/vanillons_templates',
    install_requires=[
        "PasteScript>=1.7.3"
    ],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    
    zip_safe=False,
    
    license = "MIT License",
    
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet',
    ],
    
    entry_points="""
    [paste.paster_create_template]
    vanillons = templates:VanillonsTemplate
    """
    
)
