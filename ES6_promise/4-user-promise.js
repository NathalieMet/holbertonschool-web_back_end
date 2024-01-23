import { uploadPhoto, createUser } from './utils';

export default function signUpUser(firstName, lastName) {
	return new Promise((resolve) => {
		if (firstName && lastName) {
		  resolve({ firstName: firstName, lastName: lastName});
		}
	  });
}
