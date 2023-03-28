{% macro transform_room_type(room_type) -%}
  case {{ room_type }}
    when 'Private room' then 'private'
    when 'Entire home/apt' then 'entire'
    when 'Shared room' then 'shared'
  end
{%- endmacro %}