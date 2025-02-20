/**
 * @param {string} id - A ID for use in the id and name attributes.
 * @returns {string} Markup for a checkbox.
 */
function checkbox( id ) {
  return `
    <div class="m-form-field m-form-field__checkbox">
      <input class="a-checkbox" type="checkbox" id="${ id }" name="${ id }">
      <label class="a-label" for="${ id }">
        <span>${ id }</span>
      </label>
    </div>
  `;
}

export default checkbox;
