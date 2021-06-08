SELECT MOD(task_id, {X}) AS task_base_id FROM tasks WHERE task_id >= {X}
UNION
SELECT task_base_id FROM (
  SELECT MAX (done.task_base_id) + 1 as task_base_id from (
    SELECT MOD(task_id, {X}) AS task_base_id FROM tasks
  ) AS done
) AS first_not_done WHERE task_base_id < {X};
