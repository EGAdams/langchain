#ifndef TestClassDeleteMe_H
#define TestClassDeleteMe_H

#include <string>

class TestClassDeleteMe {
public:
    // Constructor
    TestClassDeleteMe();

    // Destructor
    ~TestClassDeleteMe();

    // Example of a method declaration
    void methodName( int parameterName );

    // Example of a short method
    bool isAdministrator() { 
        bool _isAdmin = true;
        return _isAdmin; }

    // Example of a longer method
    void writeToFile( std::string textToWrite ) {
        printf( "writing to file..." );
        // fileObject.writeFile( textToWrite );
        return; }
    
    // Example of a property declaration
    // int propertyName;
};

#endif // TestClassDeleteMe_H