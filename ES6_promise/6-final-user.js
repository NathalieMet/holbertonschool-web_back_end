import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

const handleProfileSignup = async (firstName, lastName, fileName) => {
  const resultArray = [];
  try {
    const user = await signUpUser(firstName, lastName);
    resultArray.push({ status: 'fulfilled', value: user });
    await uploadPhoto(fileName);
  } catch (error) {
    resultArray.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return resultArray;
};

export default handleProfileSignup;
