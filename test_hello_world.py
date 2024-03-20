def test_hello_world(capsys):
    import hello_world
    hello_world.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"
