-- creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
    )
BEGIN
    DECLARE p_project_id INT;

    SELECT id INTO p_project_id
    FROM projects
    WHERE name = p_project_name;

    IF p_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        -- Récupérer l'ID du nouveau projet
        SET p_project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (project_id, user_id, score)
    VALUES (p_project_id, p_user_id, p_score)
    ON DUPLICATE KEY UPDATE score = VALUES(score);
END //
DELIMITER ;
