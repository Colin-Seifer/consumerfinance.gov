import { Filter } from './accessibility-helpers';

const page = new Filter();
const podname = "cfgov-89b5876f8-vtb68 -- /bin/bash -c"
const command = "kubectl exec -i"
const echo = "echo -e 'from v1.tests.wagtail_pages import create_test_page'"
const shell = "./cfgov/manage.py shell"

describe( 'Test for accessibility', () => {

  before( () => {
    /* We can be reasonably sure that the Wagtail admin is being used on a
      laptop screen or larger, and the table editor is wider than Cypress's
      default viewport, so we'll size the viewport appropriately */
    cy.viewport( 'macbook-13' );
    page.open();
    page.login();
    cy.exec(`${ command } ${ podname } "${ echo } | ${ shell }"`);
  } );

  beforeEach( () => {
    cy.visit( '/test-page/' );
    // inject axe-core. must be done after page is loaded.
    cy.injectAxe();
    /* Preserve the 'sessionid' cookie so it will not be cleared
    before the NEXT test starts. */
    Cypress.Cookies.preserveOnce( 'sessionid' );
    cy.viewport( 'macbook-13' );
  } );

  it( 'Test all elements on page', () => {
    // TODO: add tests for each element
    cy.checkAccessibility();
  } );
} );