from app import create_app

app = create_app()

if __name__ == '__main__':
    if app.config['ENV'] == 'development':
        app.run(debug=True)
    else:
        app.run()
