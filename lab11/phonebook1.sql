-- -- Create the PhoneBook table
-- CREATE TABLE IF NOT EXISTS PhoneBook (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     phone VARCHAR(20) NOT NULL
-- );

-- -- Function: Search by pattern
-- CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
-- RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
-- BEGIN
--     RETURN QUERY
--     SELECT * FROM PhoneBook
--     WHERE name ILIKE '%' || pattern || '%'
--        OR phone ILIKE '%' || pattern || '%';
-- END;
-- $$ LANGUAGE plpgsql;

-- Procedure: Insert or update user
CREATE OR REPLACE PROCEDURE insert_or_update_user(user_name1 TEXT, user_phone1 TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM PhoneBook WHERE user_name = user_name1) THEN
        UPDATE PhoneBook SET phone = user_phone1 WHERE user_name = user_name1;
    ELSE
        INSERT INTO PhoneBook(user_name, phone) VALUES (user_name1, user_phone1);
    END IF;
END;
$$;

-- Procedure: Batch insert with validation
CREATE OR REPLACE PROCEDURE insert_many_users(users TEXT[][], OUT invalid_entries TEXT[][])
LANGUAGE plpgsql AS $$
DECLARE
    i INT := 1;
    name TEXT;
    phone TEXT;
    temp_invalid TEXT[] := ARRAY[]::TEXT[];
BEGIN
    invalid_entries := ARRAY[]::TEXT[][];
    WHILE i <= array_length(users, 1) LOOP
        name := users[i][1];
        phone := users[i][2];

        IF phone ~ '^\d{10,15}$' THEN
            CALL insert_or_update_user(name, phone);
        ELSE
            temp_invalid := ARRAY[name, phone];
            invalid_entries := array_append(invalid_entries, temp_invalid);
        END IF;

        i := i + 1;
    END LOOP;
END;
$$;

-- Function: Get users with pagination
CREATE OR REPLACE FUNCTION get_users(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM PhoneBook
    ORDER BY id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;

-- -- Procedure: Delete by name or phone
-- CREATE OR REPLACE PROCEDURE delete_user(identifier TEXT)
-- LANGUAGE plpgsql AS $$
-- BEGIN
--     DELETE FROM PhoneBook WHERE name = identifier OR phone = identifier;
-- END;
-- $$;
