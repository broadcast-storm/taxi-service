const getters = {
    profileStatus: (state) => state.profileStatus,
    profileInfo: (state) => state.profileInfo,
    profileStats: (state) =>
        state.profileStatus === 'success'
            ? {
                  money: state.profileInfo.money,
                  energy: state.profileInfo.energy,
                  health: state.profileInfo.health,
                  status: state.profileStatus,
              }
            : { status: state.profileStatus },
}

export default getters
