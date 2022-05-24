import { Filter } from './accessibility-helpers';

const page = new Filter();

describe( 'Test for accessibility', () => {
  beforeEach( () => {
    cy.visit( '/test-page/' );
    // inject axe-core. must be done after page is loaded.
    cy.injectAxe();
  } );
  it( 'Test all elements on page', () => {
    // TODO: add tests for each element
    cy.checkAccessibility();
  } );
} );