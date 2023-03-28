{{ config(materialized='view') }}

WITH weekdays AS (
  SELECT
    CAST(realSum AS FLOAT64)          AS real_sum,
    CAST({{ transform_room_type('room_type') }} AS STRING) AS room_type,
    CAST(room_shared AS BOOL)         AS is_shared_room,
    CAST(room_private AS BOOL)        AS is_private_room,
    CAST(host_is_superhost AS BOOL)   AS is_superhost,
    CAST(multi AS BOOL)               AS is_multi_rooms,
    CAST(biz AS BOOL)                 AS is_business,
    CAST(bedrooms AS INTEGER)         AS bedrooms,
    CAST(person_capacity AS INTEGER)  AS person_capacity,
    CAST(cleanliness_rating AS INTEGER)          AS cleanliness_rating,
    CAST(guest_satisfaction_overall AS INTEGER)  AS guest_satisfaction_rating,
    CAST(dist AS FLOAT64)             AS central_distance,
    CAST(metro_dist AS FLOAT64)       AS metro_distance,
    CAST(lng AS FLOAT64)              AS longitude,
    CAST(lat AS FLOAT64)              AS latitude,
    'Rome'                            AS city,
    FALSE                             AS is_weekend,
  FROM `dtc-airbnb`.staging.rome_weekdays
),
weekends AS (
  SELECT
    CAST(realSum AS FLOAT64)          AS real_sum,
    CAST({{ transform_room_type('room_type') }} AS STRING) AS room_type,
    CAST(room_shared AS BOOL)         AS is_shared_room,
    CAST(room_private AS BOOL)        AS is_private_room,
    CAST(host_is_superhost AS BOOL)   AS is_superhost,
    CAST(multi AS BOOL)               AS is_multi_rooms,
    CAST(biz AS BOOL)                 AS is_business,
    CAST(bedrooms AS INTEGER)         AS bedrooms,
    CAST(person_capacity AS INTEGER)  AS person_capacity,
    CAST(cleanliness_rating AS INTEGER)           AS cleanliness_rating,
    CAST(guest_satisfaction_overall AS INTEGER)   AS guest_satisfaction_rating,
    CAST(dist AS FLOAT64)             AS central_distance,
    CAST(metro_dist AS FLOAT64)       AS metro_distance,
    CAST(lng AS FLOAT64)              AS longitude,
    CAST(lat AS FLOAT64)              AS latitude,
    'Rome'                            AS city,
    TRUE                              AS is_weekend,
  FROM `dtc-airbnb`.staging.rome_weekends
)

SELECT * FROM weekdays
UNION ALL
SELECT * FROM weekends
